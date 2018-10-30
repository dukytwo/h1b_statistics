import sys
import csv

def top_count_by_group_write_to_csv(count_by_group, csv_filename, group_field_name,
                                    top_n = 10):
    #copy data so as to keep the original data
    cbg = count_by_group.copy()
    #count total and exit if total <= 0
    count_total = sum(cbg.values())
    if count_total <= 0:
        print('count_by_group_write_to_csv: no data or 0 count in total, no output')
        return
    #add percentage to dict element as a list of [count, percentage string]
    for group, count in cbg.items():
        percentage = round(100.0*count/count_total, 1)
        cbg[group] = [count, str(percentage) + '%']
    #sort by count (reverse) and then group name
    cbg_sorted = sorted(cbg.items(),
                        key=lambda x: (-x[1][0], x[0]))
    #write to csv with header and then data
    print('Saving to file '+csv_filename)
    with open(csv_filename, 'w') as f_out:
        csv_out = csv.writer(f_out, delimiter=';',
                             quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_out.writerow([group_field_name,
                          'NUMBER_CERTIFIED_APPLICATIONS', 
                          'PERCENTAGE'])
        for i, item in enumerate(cbg_sorted, start = 1):
            csv_out.writerow([item[0], item[1][0], item[1][1]])
            if i >= top_n:
                break
    f_out.close()
    print('Saved to file '+csv_filename)

def count_by_groups_from_h1b_stat_file(filename_input, csv_delimiter,
                                       visa_status_colname,
                                       visa_status_certified_str,
                                       fields_to_group):
    print('Reading file ' + filename_input)
    with open(filename_input) as f_in:
        csv_in = csv.reader(f_in, delimiter=csv_delimiter, quotechar='"')
        #read header
        colnames = next(csv_in)
        #if the file is the old H1B_FY_2014.csv, modify its column names to be
        #compatible with the newer ones, whose column names seem consistent
        for i, colname in enumerate(colnames):
            if colname == 'STATUS':
                colnames[i] = 'CASE_STATUS'
                print('Warning: column name '+colname+' is changed to '+colnames[i])
            if colname == 'LCA_CASE_SOC_NAME':
                colnames[i] = 'SOC_NAME'
                print('Warning: column name '+colname+' is changed to '+colnames[i])
            if colname == 'LCA_CASE_WORKLOC1_STATE':
                colnames[i] = 'WORKSITE_STATE'
                print('Warning: column name '+colname+' is changed to '+colnames[i])
        #find the indicies of required fields
        visa_status_index = colnames.index(visa_status_colname)
        groups_indices = [-1]*len(fields_to_group)
        for i, field_name in enumerate(fields_to_group):
            groups_indices[i] = colnames.index(fields_to_group[i])
        #read file line by line and aggregate counts for each group
        list_of_count_by_groups = [dict() for x in range(len(groups_indices))]
        for items in csv_in:
            if items[visa_status_index] == visa_status_certified_str:
                for i, group_index in enumerate(groups_indices):
                    group_name = items[group_index]
                    if group_name in list_of_count_by_groups[i]:
                        list_of_count_by_groups[i][group_name] += 1
                    else:
                        list_of_count_by_groups[i][group_name] = 1
    f_in.close()
    print('Done read file ' + filename_input)
    return(list_of_count_by_groups)

def main():
    if(len(sys.argv) != 4):
        print('Argument error\n')
        return
    filename_input, filename_output1, filename_output2 = sys.argv[1:]
    count_by_occupation, count_by_state = count_by_groups_from_h1b_stat_file \
                            (filename_input, ';',
                             visa_status_colname = 'CASE_STATUS', 
                             visa_status_certified_str = 'CERTIFIED',
                             fields_to_group = ['SOC_NAME', 'WORKSITE_STATE'])
    top_count_by_group_write_to_csv(count_by_occupation, filename_output1,
                                    'TOP_OCCUPATIONS')
    top_count_by_group_write_to_csv(count_by_state, filename_output2,
                                    'TOP_STATES')

if __name__ == '__main__':
    main()

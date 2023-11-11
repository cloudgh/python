def convert_date_to_dict(date_str):

    year, month, day = date_str.split('-')
    

    date_dict = {
        'year': year,
        'month': month,
        'day': day
    }
    
    return date_dict


date_str = '2023-11-11'
result_dict = convert_date_to_dict(date_str)
print(result_dict)
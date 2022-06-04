from fastapi import FastAPI
import application

db_file_path ='/Users/roopeshbharatwajkr/EduPycharmProjects/roopesh/Fast_API/AS_Database.db'
tsv_file='/Users/roopeshbharatwajkr/EduPycharmProjects/roopesh/Fast_API/ip2asn-v4.tsv'

app = FastAPI()
@app.get("/fetch_data/{as_number}")
async def fetch_data(as_number):
    DataFrame=application.read_tsv_file(tsv_file)
    connection = application.connect_database(db_file_path, DataFrame)
    rows = application.get_as_from_as_number(connection,as_number)
    # data_new= application.filter_get_as_info(connection, number)
    return rows

@app.get("/fetch_ip/{ip_range_start}")
async def fetch_ip(ip_range_start):
    DataFrame=application.read_tsv_file(tsv_file)
    connection = application.connect_database(db_file_path, DataFrame)
    rows= application.get_as_from_ip_range(connection,ip_range_start)
    return rows



# if __name__ == '__main__':
#     DataFrame=application.read_tsv_file(tsv_file)
#     connection = application.connect_database(db_file_path, DataFrame)
#     rows= application.to_view(connection)
#     print(rows[-1])




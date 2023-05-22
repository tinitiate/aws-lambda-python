import boto3
from botocore.exceptions import ClientError
import os

# params = config('config.ini','aws')
# profile_name = params.get('profile')


boto3.setup_default_session(profile_name='sbadmin')
s3_client = boto3.client('s3')

def download_s3_file(p_s3_bucket_name, p_s3_folder,p_s3_file_name,p_local_download_folder_file):

    l_s3_file_path_name = p_s3_folder+"/"+p_s3_file_name
    s3_client.download_file(p_s3_bucket_name, l_s3_file_path_name, p_local_download_folder_file)


def upload_my_file(p_s3_bucket_name, p_s3_folder, p_local_folder_file_to_upload, p_upload_file_name = "N/A"):

    l_s3_file_name = ""
    
    if p_upload_file_name == "N/A":
        l_s3_file_name = p_s3_folder + "/" + os.path.basename(p_local_folder_file_to_upload)
    else:
        l_s3_file_name = p_s3_folder + "/" + p_upload_file_name
    
    try:
        response = s3_client.upload_file(p_local_folder_file_to_upload, p_s3_bucket_name, l_s3_file_name)
    except ClientError as e:
        print(e)
        return False
    except FileNotFoundError as e:
        print(e)
        return False
    return True

def main():
    l_s3_bucket='sb-events-s3-bucket'
    l_s3_data_folder='csv'
    l_s3_scripts_folder='scripts/db'
    l_local_folder_file_to_upload='E:/code/PYTHON_TRAINING/modules/s3/data.csv'
    l_file_name= 'customers.csv'
    # Test 1
    upload_my_file(l_s3_bucket, l_s3_data_folder, l_local_folder_file_to_upload, l_file_name)
    # Test 2
    # upload_my_file(l_s3_bucket, l_s3_data_folder, l_local_folder_file_to_upload)

    # download_s3_file(l_s3_bucket, l_s3_data_folder, "loan_rules.csv","E:\\code\\PYTHON_TRAINING\\Python_AWS\\loan.csv")
    # download_s3_file(l_s3_bucket, l_s3_data_folder, "loan_rules.json","E:\\code\\PYTHON_TRAINING\\Python_AWS\\rules.json")
    # download_s3_file(l_s3_bucket, l_s3_data_folder, "rules.xml","E:\\code\\PYTHON_TRAINING\\Python_AWS\\rules.xml")
    # download_s3_file(l_s3_bucket, l_s3_scripts_folder, "billing_db.sql","E:\\code\\PYTHON_TRAINING\\Python_AWS\\Retail_DDL_AWS_SQL.sql.sql")


if __name__ == '__main__' :main()

#Upload file
#upload_my_file("python-100", "cbuser1/scripts", "/SyntaxBoard/aws-scripts/test.txt", "test.txt")
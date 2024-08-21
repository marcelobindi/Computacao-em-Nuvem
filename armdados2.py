def store_data_in_aws(student_id, presence_status):
    table.put_item(
        Item={
            'student_id': student_id,
            'presence': presence_status,
            'timestamp': int(time.time())
        }
    )
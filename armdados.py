def store_data_in_firebase(student_id, presence_status):
    doc_ref = db.collection('attendance').document(student_id)
    doc_ref.set({
        'student_id': student_id,
        'presence': presence_status,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
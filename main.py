from src.predict import predict_job

job_text = input("Enter job description: ")
result = predict_job(job_text)
print(result)

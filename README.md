# simple_s3_manager_API

A simple API for storing binary data in AWS s3 service.
Data is accessed by key (file name) without extension.

# Installing using Github

    git clone https://github.com/taras-andruschenko/simple_s3_manager_API.git
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python.exe -m uvicorn main:app --reload

# How to use

To use this API you should have an Amazon S3 account. If you don't have an account there,
visit https://s3.console.aws.amazon.com/s3 for more detail and additional information.
    
By default, after <Installing> API has address http://127.0.0.1:8000/
Just visit http://127.0.0.1:8000/docs to see an OpenAPI documentation and try it out.

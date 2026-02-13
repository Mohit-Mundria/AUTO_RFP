#script binds the app to all network interfaces, allowing you to access it from your browser via the EC2 Public IP.

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

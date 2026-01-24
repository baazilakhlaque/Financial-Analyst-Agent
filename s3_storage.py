import boto3
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class S3Storage:
    """Utility class for uploading files to AWS S3."""
    
    def __init__(self):
        self.access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.region = os.getenv("AWS_REGION", "us-east-1")
        self.bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
        
        # Validate required environment variables
        if not all([self.access_key, self.secret_key, self.bucket_name]):
            raise ValueError(
                "Missing AWS credentials. Please set AWS_ACCESS_KEY_ID, "
                "AWS_SECRET_ACCESS_KEY, and AWS_S3_BUCKET_NAME in .env"
            )
        
        # Initialize S3 client
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )
    
    def upload_file(
        self, 
        local_file_path: str, 
        s3_key: Optional[str] = None,
        make_public: bool = False
    ) -> str:
        """
        Upload a file to S3.
        
        Args:
            local_file_path: Path to the local file to upload
            s3_key: S3 object key (path in bucket). If None, uses filename with timestamp
            make_public: Whether to make the file publicly accessible
        
        Returns:
            S3 URL of the uploaded file
        """
        if not os.path.exists(local_file_path):
            raise FileNotFoundError(f"File not found: {local_file_path}")
        
        # Generate S3 key if not provided
        if s3_key is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = Path(local_file_path).name
            s3_key = f"plots/{timestamp}_{filename}"
        
        try:
            # Upload file
            extra_args = {}
            if make_public:
                extra_args['ACL'] = 'public-read'
            
            self.s3_client.upload_file(
                local_file_path,
                self.bucket_name,
                s3_key,
                ExtraArgs=extra_args
            )
            
            # Generate URL
            url = f"https://{self.bucket_name}.s3.{self.region}.amazonaws.com/{s3_key}"
            
            return url
            
        except Exception as e:
            raise Exception(f"Failed to upload file to S3: {str(e)}")
    
    def upload_plot_files(self, directory: str = ".") -> list[dict]:
        """
        Find and upload all PNG plot files in a directory.
        
        Args:
            directory: Directory to search for PNG files (default: current directory)
        
        Returns:
            List of dictionaries with 'filename' and 's3_url' keys
        """
        uploaded_files = []
        directory_path = Path(directory)
        
        # Find all PNG files
        png_files = list(directory_path.glob("*.png"))
        
        for png_file in png_files:
            try:
                s3_url = self.upload_file(str(png_file))
                uploaded_files.append({
                    'filename': png_file.name,
                    's3_url': s3_url,
                    'local_path': str(png_file)
                })
            except Exception as e:
                print(f"Warning: Failed to upload {png_file.name}: {e}")
        
        return uploaded_files


# Convenience function for easy usage
def upload_plots_to_s3(directory: str = ".") -> list[dict]:
    """Convenience function to upload all plots in a directory to S3."""
    storage = S3Storage()
    return storage.upload_plot_files(directory)
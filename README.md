# HarmonyTune Spotify-API-Data-Analysis

## Introduction
The Spotify ETL (Extract, Transform, Load) project is a data pipeline that fetches data from the Spotify API, performs data transformation, and loads the transformed data into an Amazon S3 bucket. The pipeline focuses on extracting information about albums, songs, and artists from a specified Spotify playlist, transforming the raw data into a structured format, and storing it for further analysis and processing.

## Architecture 
<img src="https://github.com/krishna7356/HarmonyTune---Spotify-API-Data-Analysis/blob/main/spotify-ETL.jpeg">

## Technology used
- Programming Language - Python
- Amazon Web Service (AWS)
1. S3 (Simple Storage Service)
2. Athena
3. Glue Crawler
4. Glue Catalog
5. Cloud Watch
6. Lambda

## High-Level Overview

- Data Extraction: The Spotify API is accessed using the Spotipy library, which handles the authentication process using client credentials. The API request retrieves data about albums, songs, and artists from a specified Spotify playlist.

- Data Transformation: The raw data obtained from the API is transformed using the Pandas library in Python. The transformation process involves parsing the raw data, organizing it into structured dataframes, and performing any necessary data manipulations. This step ensures that the data is in a suitable format for further analysis.

- Data Loading: The transformed data is saved as CSV files, which provide a structured representation of the albums, songs, and artists. The data is loaded into an Amazon S3 bucket, which acts as a central repository for storing both the raw and transformed data. The S3 bucket provides scalability, durability, and easy access to the data.

- Automated Data Processing: The project incorporates automation using AWS services. AWS Lambda is used to trigger the data extraction and transformation process periodically. This can be achieved by configuring CloudWatch Events to trigger the Lambda function at specified intervals, ensuring that the data is regularly fetched and updated.

- Data Analysis and Insights: With the transformed data stored in the S3 bucket, it can be further analyzed and processed. AWS Glue Crawler can automatically discover and catalog the transformed CSV files in the S3 bucket, making it easier to integrate with Amazon Athena. Amazon Athena allows running SQL queries on the transformed data stored in S3, enabling ad-hoc analysis and generating insights without the need for complex infrastructure setup.

# PDF Bundle

This take-home project has been designed within a timeframe of less than 72 hours, serving as a step in the hiring process for a Senior MLOps role.

PDF Bundle is a tool designed to extract text from PDF documents stored in an AWS S3 bucket, break down these documents into smaller pieces, and generate vector embeddings using Sentence Transformer. These embeddings are then stored in a Pinecone vector database for efficient storage and retrieval.

PDF Bundle provides a user-friendly interface through FastAPI. The `query_search` endpoint facilitates prompt-based searches, allowing users to input queries and swiftly retrieve the most similar vector embeddings. This similarity is determined using cosine similarity, a measure that captures the semantic similarity between vectors. While simplifying the response for usability, PDF Bundle ensures transparency by automatically uploading detailed responses to the S3 bucket. With its seamless integration and robust functionality, PDF Bundle efficiently uncovers the most similar vector embeddings.

## Features

- Extract text from PDF documents stored in AWS S3 bucket.
- Split documents into smaller pieces for efficient processing.
- Utilize Sentence Transformer to generate vector embeddings for each document piece.
- Use FastAPI to create an API endpoint for querying similar embeddings based on user-defined prompts.
- Store and query vector embeddings in a Pinecone vector database for easy management and retrieval.
- Allow users to find the most similar k vectors by assigning an integer n_top.

## Usage

1. Ensure that the PDF Bundle API server is running on the following server:
   
   The application is deployed and accessible at: [Railway](https://pdf-bundle-production.up.railway.app/docs).

   Warning: Free Instance Spin-Down Delay

   Please note that the free instance provided by Render may experience spin-down due to inactivity. This could result in delays of 50 seconds or more when processing requests. Please be patient while your web browser tries to load the page.

3. Send a POST request to the API endpoint `/query_search` with the following JSON payload:

    ```json
    {
        "prompt": "your_user_defined_prompt",
        "n_top": 5
    }
    ```

    Replace `"your_user_defined_prompt"` with the prompt you want to use, `"n_top"` with the number of similar embeddings you want to retrieve based on cosine simuilarity.

4. Receive a response containing the most similar embeddings to the provided prompt.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.

## Acknowledgments

- [AWS SDK for Python (Boto3)](https://github.com/boto/boto3)
- [Sentence Transformers](https://www.sbert.net/examples/applications/computing-embeddings/README.html)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Pinecone](https://www.pinecone.io/)

## Contact

For any inquiries or support, please contact ozerozdal@gmail.com

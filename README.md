# PDF Bundle

PDF Bundle is a tool designed to extract text from PDF documents stored in an AWS S3 bucket, break down these documents into smaller pieces, and generate vector embeddings using Sentence Transformer. These embeddings are then stored in a Pinecone vector database for efficient storage and retrieval.

## Features

- Extract text from PDF documents stored in AWS S3 bucket.
- Split documents into smaller pieces for efficient processing.
- Utilize Sentence Transformer to generate vector embeddings for each document piece.
- Use FastAPI to create an API endpoint for querying similar embeddings based on user-defined prompts.
- Store and query vector embeddings in a Pinecone vector database for easy management and retrieval.
- Allow users to find the most similar k vectors by assigning an integer n_top.

## Usage

1. Ensure that the PDF Bundle API server is running on the following server:
   
   [PDF Bundle API Server](http://pdfbundlealb-669840896.us-east-1.elb.amazonaws.com/docs#/default/query_search_query_search_post)

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

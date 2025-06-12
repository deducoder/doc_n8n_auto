import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [apiStatus, setApiStatus] = useState("Connecting...");
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadStatus, setUploadStatus] = useState<string>("");
  const [isDragging, setIsDragging] = useState(false);

  useEffect(() => {
    const fetchApiStatus = async () => {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/health`);
        if (response.ok) {
          const data = await response.json();
          console.log(data);
          setApiStatus(data.message || "API is running");
        } else {
          setApiStatus("API is not reachable");
        }
      } catch (error) {
        setApiStatus("Error connecting to API");
      }
    };
    fetchApiStatus();
  }, []);

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
      setUploadStatus("");
    }
  };

  const handleDragOver = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    setIsDragging(false);
  };

  const handleDrop = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    setIsDragging(false);
    const file = event.dataTransfer.files?.[0];
    if (file) {
      setSelectedFile(file);
      setUploadStatus("");
    }
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadStatus("Please select a file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      setUploadStatus("Uploading...");
      const response = await fetch(`${import.meta.env.VITE_API_URL}/upload`, {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        setUploadStatus("File uploaded successfully!");
        setSelectedFile(null);
        console.log(data);
      } else {
        setUploadStatus("Failed to upload file");
      }
    } catch (error) {
      setUploadStatus("Error uploading file");
    }
  };

  return (
    <div className="container">
      <h1>{apiStatus}</h1>
      <h1>Welcome to the React App</h1>

      <div
        className={`upload-area ${isDragging ? "dragging" : ""}`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          onChange={handleFileSelect}
          style={{ display: "none" }}
          id="fileInput"
        />
        <label htmlFor="fileInput" className="upload-button">
          Choose File
        </label>
        <p>or drag and drop your file here</p>
        {selectedFile && (
          <div className="selected-file">
            <p>Selected file: {selectedFile.name}</p>
            <button onClick={handleUpload}>Upload</button>
          </div>
        )}
        {uploadStatus && <p className="upload-status">{uploadStatus}</p>}
      </div>
    </div>
  );
}

export default App;

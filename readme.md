This project provides a server application that integrates **MongoDB Atlas** with the **Application Development Kit (ADK)** using mongodb-mcp-server. It enables secure, scalable, and efficient data management through RESTful APIs, leveraging service account authentication and robust error handling. The server is designed to accelerate development workflows by simplifying integration with MongoDB Atlas and providing a ready-to-use backend for your applications.

---

## 🚀 Features

- **Secure Connection:** Connects to MongoDB Atlas using a service account client ID and client secret.
- **ADK Integration:** Utilizes the ADK to simplify integration and accelerate development.
- **Authentication & Authorization:** Supports secure authentication using service account credentials.
- **Robust Error Handling:** Provides detailed logging for easier debugging and maintenance.
- **Scalable Data Management:** Enables efficient data operations with MongoDB Atlas.
- **RESTful API:** Exposes endpoints for CRUD operations.

---

## 📦 Prerequisites

-google-adk


---

## ⚡ Installation

```bash
git clone https://github.com/yourusername/mongodb_mcp_server.git
cd mongodb_mcp_server
```

---

## ⚙️ Configuration

Configure your project to connect to MongoDB Atlas:

```json
{
    "mcpServers": {
        "MongoDB": {
            "command": "npx",
            "args": [
                "-y",
                "mongodb-mcp-server",
                "--apiClientId",
                "your-atlas-service-accounts-client-id",
                "--apiClientSecret",
                "your-atlas-service-accounts-client-secret"
            ]
        }
    }
}
```

---

## ▶️ Usage

Start the web UI:

```bash
adk web
```

The server will run at [http://localhost:8080](http://localhost:8080) by default.

---


---

## 📄 License

[MIT](LICENSE)

// server.js
import express from "express";
import dotenv from "dotenv";
import axios from "axios";

dotenv.config();

const app = express();
app.use(express.json());

const HOME_SERVER_URL = process.env.HOME_SERVER_URL;
if (!HOME_SERVER_URL) {
    throw new Error("HOME_SERVER_URL not set in .env");
}

app.post("/sendURL", async (req, res) => {
    try {
        const { imageUrl } = req.body;
        const response = await axios.post(HOME_SERVER_URL, { imageUrl });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.get("/", (req, res) => {
    res.json({ message: "Hello from Vercel!" });
});

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

export default app;

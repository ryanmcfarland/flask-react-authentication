import React, { useState } from "react";

const RegisterPage = () => {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const registerUser = async () => {
        const formData = new FormData();
        formData.append("email", email);
        formData.append("username", username);
        formData.append("password", password);
        try {
            const resp = await fetch("/auth/register", { body: formData, method: "post" });
            if (!resp.ok) {
                throw new Error("Invalid");
            }
            window.location.href = "/";
        } catch (error) {
            if (error.response.status === 401) {
                alert("Invalid credentials");
            }
        }
    };

    return (
        <div>
            <h1>Create an account</h1>
            <form>
                <div>
                    <label>Username: </label>
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} id="" />
                </div>
                <div>
                    <label>Email: </label>
                    <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} id="" />
                </div>
                <div>
                    <label>Password: </label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="" />
                </div>
                <button type="button" onClick={registerUser}>
                    Submit
                </button>
            </form>
        </div>
    );
};

export default RegisterPage;

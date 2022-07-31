import React, { useState } from "react";

const LoginPage = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const logInUser = async () => {
        console.log(email, password);
        const formData = new FormData();
        formData.append("username", email);
        formData.append("password", password);

        try {
            const resp = await fetch("/auth/login", { body: formData, method: "post" });
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
            <h1>Log Into Your Account</h1>
            <form>
                <div>
                    <label>Email: </label>
                    <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} id="" />
                </div>
                <div>
                    <label>Password: </label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="" />
                </div>
                <button type="button" onClick={logInUser}>
                    Submit
                </button>
            </form>
        </div>
    );
};

export default LoginPage;

import React, { useState, useEffect } from "react";

const LandingPage = () => {
    const [user, setUser] = useState(null);

    const logoutUser = async () => {
        await fetch("/auth/logout");
        window.location.href = "/";
    };

    useEffect(() => {
        (async () => {
            try {
                const resp = await fetch("/username", { method: "get" });
                if (!resp.ok) {
                    throw new Error("Invalid");
                }
                setUser(await resp.json());
            } catch (error) {
                console.log("Not authenticated");
            }
        })();
    }, []);

    return (
        <div>
            <h1>Welcome to this React Application</h1>
            {console.log(user)}
            {user != null ? (
                <div>
                    <h2>Logged in</h2>
                    <h3>ID: {user.username}</h3>

                    <button onClick={logoutUser}>Logout</button>
                </div>
            ) : (
                <div>
                    <p>You are not logged in</p>
                    <div>
                        <a href="/login">
                            <button>Login</button>
                        </a>
                        <a href="/register">
                            <button>Register</button>
                        </a>
                    </div>
                </div>
            )}
        </div>
    );
};

export default LandingPage;

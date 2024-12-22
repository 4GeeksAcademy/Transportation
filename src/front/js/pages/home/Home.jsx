import React from "react";
import { Navbar } from "../../components/Navbar";

export const Home = () => {
    return (
        <div className="d-flex flex-column min-vh-100">
            <Navbar />
            <div className="container mt-4">
                <h1 className="display-4">Welcome to Transportation</h1>
            </div>
        </div>
    );
}; 
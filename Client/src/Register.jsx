import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleRegister = () => {
        axios.post(`${import.meta.env.VITE_API_URL}/register`, { username, password })
            .then(res => {
                setMessage('Registered successfully! Redirecting to login...');
                setError('');
                setTimeout(() => navigate('/login'), 2000);
            })
            .catch(err => {
                setError(err.response?.data?.error || 'Registration failed');
                setMessage('');
            });
    };

    return (
        <div className='container mt-5' style={{ maxWidth: '400px' }}>
            <h2 className='mb-4 text-center'>Register</h2>
            {error && <div className='alert alert-danger'>{error}</div>}
            {message && <div className='alert alert-success'>{message}</div>}
            <div className='mb-3'>
                <label className='form-label'>Username</label>
                <input
                    type='text'
                    className='form-control'
                    value={username}
                    onChange={e => setUsername(e.target.value)}
                />
            </div>
            <div className='mb-3'>
                <label className='form-label'>Password</label>
                <input
                    type='password'
                    className='form-control'
                    value={password}
                    onChange={e => setPassword(e.target.value)}
                />
            </div>
            <button className='btn btn-success w-100' onClick={handleRegister}>Register</button>
            <p className='mt-3 text-center'>
                Already have an account? <Link to='/login'>Login</Link>
            </p>
        </div>
    );
};

export default Register;
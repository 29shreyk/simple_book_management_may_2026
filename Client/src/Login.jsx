import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = () => {
        axios.post(`${import.meta.env.VITE_API_URL}/login`, { username, password })
            .then(res => {
                localStorage.setItem('token', res.data.access_token);
                navigate('/');
            })
            .catch(err => {
                setError('Invalid username or password');
            });
    };

    return (
        <div className='container mt-5' style={{ maxWidth: '400px' }}>
            <h2 className='mb-4 text-center'>Login</h2>
            {error && <div className='alert alert-danger'>{error}</div>}
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
            <button className='btn btn-primary w-100' onClick={handleLogin}>Login</button>
            <p className='mt-3 text-center'>
                Don't have an account? <Link to='/register'>Register</Link>
            </p>
        </div>
    );
};

export default Login;
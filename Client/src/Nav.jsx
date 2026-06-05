import React from 'react'
import { useNavigate } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css'

const Nav = () => {
    const navigate = useNavigate()
    const token = localStorage.getItem('token')

    const handleLogout = () => {
        localStorage.removeItem('token')
        navigate('/login')
    }

    return (
        <div className='d-flex justify-content-between align-items-center py-2 px-4 shadow-sm'>
            <div className='fs-2 fw-bold'>Book Management System</div>
            {token && (
                <button className='btn btn-danger' onClick={handleLogout}>
                    Logout
                </button>
            )}
        </div>
    )
}

export default Nav
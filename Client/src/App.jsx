import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Books from './Books';
import CreateBook from './CreateBook';
import UpdateBook from './UpdateBook';
import Login from './Login';
import Register from './Register';
import Nav from './Nav';

const PrivateRoute = ({ children }) => {
    const token = localStorage.getItem('token');
    return token ? children : <Navigate to='/login' />;
};

function App() {
    return (
        <BrowserRouter>
            <Nav />
            <Routes>
                <Route path='/login' element={<Login />} />
                <Route path='/register' element={<Register />} />
                <Route path='/' element={<PrivateRoute><Books /></PrivateRoute>} />
                <Route path='/create' element={<PrivateRoute><CreateBook /></PrivateRoute>} />
                <Route path='/update' element={<PrivateRoute><UpdateBook /></PrivateRoute>} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;
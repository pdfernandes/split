import React, { useState } from 'react';

const SignInForm = (props) => {
  const [ username, setUsername ] = useState('');
  const [ password, setPassword ] = useState('');

  const handleUsernameChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleSubmit = async (event) => {
    event.preventDefault();
    const credentials = { username, password };
    const response = await fetch('http://localhost:8000/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(credentials)
    });
    
    if (response.status === 200) {
      const token = await response.json();
      console.log('LOGIN SUCCESS', token);
    } else {
      const info = await response.json();
      console.log('LOGIN FAIL', info.detail);
    }
  };

  return <>
    <form onSubmit={handleSubmit}>
      <label>username </label>
      <input type="text" value={username} onChange={handleUsernameChange} />
      <label>password </label>
      <input type="password" value={password} onChange={handlePasswordChange} />
      <button>sign in</button>
    </form>
  </>;
};

export default SignInForm;
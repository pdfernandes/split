import React, { useState } from 'react';

const SignUpForm = (props) => {
  const [ email, setEmail ] = useState('');
  const [ username, setUsername ] = useState('');
  const [ password, setPassword ] = useState('');

  const handleEmailChange = (event) => setEmail(event.target.value);
  const handleUsernameChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handleSubmit = async (event) => {
    event.preventDefault();
    const newUserCredentials = { email, username, password };
    const response = await fetch('http://localhost:8000/api/user/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newUserCredentials)
    });
    
    if (response.status === 201) {
      console.log('SIGN UP SUCCESS', await response.json());
    } else {
      console.log('SIGN UP FAIL', await response.json());
    }
  };

  return <>
    <form onSubmit={handleSubmit}>
      <label>email </label>
      <input type="email" value={email} onChange={handleEmailChange} />
      <label>username </label>
      <input type="text" value={username} onChange={handleUsernameChange} />
      <label>password </label>
      <input type="password" value={password} onChange={handlePasswordChange} />
      <button>sign up</button>
    </form>
  </>;
};

export default SignUpForm;
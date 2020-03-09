import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import SignInForm from './SignInForm';
import SignUpForm from './SignUpForm';

const App = () => {
  return <>
    <Router>
      <Switch>
        <Route path="/signin">
          <SignInForm />
        </Route>
        <Route path="/signup">
          <SignUpForm />
        </Route>
      </Switch>
    </Router>
  </>;
};

export default App;
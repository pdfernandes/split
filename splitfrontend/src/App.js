import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

const App = () => {
  return <>
    <h2>app</h2>
    <Router>
      <Switch>
        <Route path="/signin">
          signin!!
        </Route>
        <Route path="/signup">
          signup!!
        </Route>
      </Switch>
    </Router>
  </>;
};

export default App;
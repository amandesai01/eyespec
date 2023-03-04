import { useState } from "react";
import {
  BrowserRouter as Router,
  Redirect,
  Route,
  Switch,
} from "react-router-dom";
import "./App.css";
import Home from "./components/Home";
import Login from "./components/Login";

function App() {
  const [user, setUser] = useState();
  return (
    <>
      <Router>
        <Switch>
          <Route exact path={"/(index.html)?"}>
            <Login setUser={setUser} />
          </Route>
          <Route exact path={"/Home"}>
            {/* {user ? <Home /> : <Redirect to={"/"} />} */}
            <Home />
          </Route>
        </Switch>
      </Router>
    </>
  );
}

export default App;

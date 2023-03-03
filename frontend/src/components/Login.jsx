import { useState } from "react";
import sapiensImg from "./assets/sapiens.png";
import { useHistory } from "react-router-dom";

function Login({ setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const history = useHistory();

  function usernameHandler(event) {
    setUsername(event.target.value);
  }

  function passwordHandler(event) {
    setPassword(event.target.value);
  }

  function authenticateUser() {
    // if user is authenticated
    setUser({ username });
    history.push("/home");
  }

  return (
    <>
      <div className="flex items-center">
        <img
          src={sapiensImg}
          className="flex-1"
          style={{ maxWidth: "60%", backgroundColor: "#E8ECEF" }}
        />
        <div className="form-control w-full max-w-xs flex-1 ">
          <h1>Login</h1>
          <label className="label">
            <span className="label-text">Username</span>
          </label>
          <input
            type="text"
            value={username}
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs"
            onChange={(event) => usernameHandler(event)}
          />
          <label className="label">
            <span className="label-text">Password</span>
          </label>
          <input
            type="password"
            value={password}
            placeholder="Type here"
            className="input input-bordered w-full max-w-xs"
            onChange={(event) => passwordHandler(event)}
          />
          <button className="btn btn-outline" onClick={authenticateUser}>
            Button
          </button>
        </div>
      </div>
    </>
  );
}

export default Login;

function Navbar() {
  return (
    <div className="navbar bg-base-100 drop-shadow">
      <div className="flex-1">
        <a className="btn btn-ghost normal-case text-xl">Eyespec</a>
      </div>
      <div className="flex-none gap-2">
        {/* <div className="dropdown dropdown-end">
          <label tabIndex={0} className="btn btn-ghost btn-circle avatar">
            <div className="w-10 rounded-full">
              <img src="/images/stock/photo-1534528741775-53994a69daeb.jpg" />
            </div>
          </label>
          <ul
            tabIndex={0}
            className="mt-3 p-2 shadow menu menu-compact dropdown-content bg-base-100 rounded-box w-52"
          >
            <li>
              <a className="justify-between">
                Profile
                <span className="badge">New</span>
              </a>
            </li>
            <li>
              <a>Settings</a>
            </li>
            <li>
              <a>Logout</a>
            </li>
          </ul>
        </div> */}
        <button className="btn">Login</button>
      </div>
    </div>
  );
}

export default Navbar;

import { useState } from "react"

export default function Login(){

    const [userName,setUserName] = useState("username")

    function HandleChangeUser(event){
        setUserName(event.target.value)
    }

    return(
        <>
            <div className="nav">
                <h1 style={{fontWeight: "bold"}}>MyBlog</h1>
                <h2>Register</h2>
            </div>
            <div>
                <center><h1>Login</h1></center>
            </div>
            <center><div className="user_pass">
                <input type = "text" required value={userName} onChange={HandleChangeUser}/>
                <input type="text" placeholder="password"/>
                <button>Login</button>
            </div></center>
        </>
    )
}
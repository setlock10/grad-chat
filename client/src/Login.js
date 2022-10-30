import React, {useState} from 'react'


function Login({playMusic}){
    const [formData, setFormData] = useState({
        //username:'',
        email:'',
        password:''
    })
    // var logo = document.getElementById("logo")
    const [errors, setErrors] = useState([])

    const {username, email, password} = formData

    function onLogin(e){
        e.preventDefault()
        playMusic()
    }

    const handleChange = (e) => {
        const { name, value } = e.target
        setFormData({ ...formData, [name]: value })
      }
  




    return(
        <div className="login" >
            <h1 className='form-title'>Sign In</h1>
            <div className="loginBackground" ></div>
            <form className="loginForm"  onSubmit={onLogin}>
                <div>
                    <input className="inputBox" type='text' name='email' placeholder="Email Address" value={email} onChange={handleChange} />
                </div>
                <div>
                    <input className="inputBox"  type='password' name='password' placeholder="Password" value={password} onChange={handleChange} />
                </div>
                <input className="button"  type='submit' value='SIGN IN' /> 
            </form>  
            {/* <div className="divider"></div>      */}
        </div>
    )
 
 
 
 }
 export default Login;
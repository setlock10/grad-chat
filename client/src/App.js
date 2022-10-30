import { useState, useEffect,useRef } from "react";
import Login from "./Login";
import survivin from "./Bastille-survivin.mp3"


function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    fetch("/hello")
      .then((r) => r.json())
      .then((data) => setCount(data.count));
  }, []);

  const space = useRef(new Audio(survivin))

function playMusic(){

  space.current.play()
  space.current.loop = true

}


  return (
    <div className="App">
      <Login playMusic={playMusic}/>
    </div>
  );
}

export default App;
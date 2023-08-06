import DivMap from "./components/DivMap";
import {useSelector} from "react-redux";
import {getUser} from "./store/selectors/getUser";
import NavBar from "./components/NavBar";

function App() {
    const user = useSelector(getUser);
return (
    <div className="App"
    className="app-container d-flex flex-column vh-100"
    >
        <NavBar />
        <DivMap />
    </div>
  );
}

export default App;

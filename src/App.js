import logo from './logo.svg';
import './App.css';
import Data from './components/Data';
import SampleData from './components/Sample';
import E

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Data />
        <SampleData />
      </header>
    </div>
  );
}

export default App;
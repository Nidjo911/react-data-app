import './App.css';
import Data from './components/Data';
import SampleData from './components/Sample';
import Equipment from './components/EquipmentList';

export default function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Data />
        <SampleData />
        <Equipment />
      </header>
    </div>
  );
}
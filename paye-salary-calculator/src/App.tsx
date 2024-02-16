import { useState } from 'react'
import './App.css'

function App() {
  const [baseSalary, setBaseSalary] = useState(0)
  const [salary, setSalary] = useState(0)
  const [takeHome, setTakeHome] = useState(0)

  const handleChange = event => {
    if (event.target.id == 'baseSalary') {
      setBaseSalary(event.target.value);
    } else if (event.target.id === 'takeHome') {
      setTakeHome(event.target.value);
    } else if (event.target.id === 'salary') {
      setSalary(event.value.value);
    }
  };

  const calculateEpf = baseSalary => baseSalary * .08;

  const calculateTax = salary => {
    
  };

  const calculateTakeHomeSalary = (baseSalary, salary) => {
    return salary - calculateEpf(baseSalary) - calculateTax(salary);
  }


  return (
    <>
      <h2>
        Enter base salary if you pay EPF.
      </h2>
      <form>
        <input id='baseSalary' type='number' value={baseSalary} onChange={ event => handleChange(event)} ></input>
        <label htmlFor='baseSalary'>Enter base salary: </label>
        <input id='takeHome' type='number' value={takeHome} onChange={(event) => handleChange(event)}></input>
        <label htmlFor='takeHome'>Enter take home salary: </label>
        <input id='salary' type='number' value={salary} onChange={(event) => handleChange(event)}></input>
        <label htmlFor='takeHome'>Enter salary before deductions: </label>
      </form>
    </>
  )
}

export default App

import { useState } from 'react'
import './App.css'

function App() {
  const [baseSalary, setBaseSalary] = useState(0);
  const [salary, setSalary] = useState(0);
  const [takeHome, setTakeHome] = useState(0);
  const [tax, setTax] = useState(0);

  const handleChange = event => {
    if (event.target.id == 'baseSalary') {
      setBaseSalary(event.target.value);
    } else if (event.target.id === 'takeHome') {
      setTakeHome(event.target.value);
    } else if (event.target.id === 'salary') {
      setSalary(event.target.value);
    }
  };

  const calculateEpf = baseSalary => baseSalary * .08;

  const calculateTax = salary => {
    let calculatedTax = 0
    if (salary < 100000) {
        calculatedTax = 0
    }
    else if (salary < 141667) {
        calculatedTax = salary * 0.06 - 6000
    }
    else if (salary < 183333) {

        calculatedTax = salary * 0.12 - 14500
    }
    else if (salary < 225000) {

        calculatedTax = salary * 0.18 - 25500
    }
    else if (salary < 266667) {

        calculatedTax = salary * 0.24 - 39000
    }
    else if (salary < 308333) {

        calculatedTax = salary * 0.30 - 55000
    }
    else {

        calculatedTax = salary * 0.36 - 73500
    }
    setTax(calculatedTax)
  };

  const calculateTakeHomeSalary = (baseSalary, salary) => {
    if (salary !== null && baseSalary !== null) {
      calculateTax(salary);
      let calculatedTakeHome = salary - calculateEpf(baseSalary) - tax;
      setTakeHome(calculatedTakeHome)
    }
  }


  return (
    <>
      <h2>
        Enter base salary if you pay EPF.
      </h2>
      <h3>
        Enter salary to calculate take home salary after deductions.
        Enter take home salary to calculate salary before deductions.
      </h3>
      <form onSubmit={e => e.preventDefault()}>
        <input id='baseSalary' type='number' min='0' value={baseSalary} onChange={ event => handleChange(event)} ></input>
        <label htmlFor='baseSalary'>Enter base salary: </label>
        <input id='salary' type='number' min='0' value={salary} onChange={(event) => handleChange(event)}></input>
        <label htmlFor='salary'>Enter salary before deductions: </label>
        <button onClick={ () => {
          calculateTakeHomeSalary(baseSalary, salary)
        }}>Click me!</button>
        <span>Take home salary: {takeHome || '0'}</span>
      </form>
    </>
  )
}

export default App

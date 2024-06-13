import React, { useState, useEffect } from 'react';

const ExchangeRates = () => {
  const [exchangeRates, setExchangeRates] = useState({});
  const [availableCurrencies, setAvailableCurrencies] = useState([]);
  const [selectedCurrency, setSelectedCurrency] = useState('');

  useEffect(() => {
    const fetchAvailableCurrencies = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/available-currencies');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setAvailableCurrencies(data.currencies || []);
      } catch (error) {
        console.error('Error fetching available currencies:', error);
      }
    };

    fetchAvailableCurrencies();
  }, []);

  const fetchExchangeRates = async (baseCurrency) => {
    try {
      const response = await fetch(`http://localhost:8000/api/exchange-rates/${baseCurrency}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setExchangeRates(data);
    } catch (error) {
      console.error('Error fetching exchange rates:', error);
    }
  };

  const handleCurrencyChange = (e) => {
    const baseCurrency = e.target.value;
    setSelectedCurrency(baseCurrency);
    fetchExchangeRates(baseCurrency);
  };

  return (
    <div>
      <h1>Exchange Rates</h1>
      <select value={selectedCurrency} onChange={handleCurrencyChange}>
        <option value="">Select Currency</option>
        {availableCurrencies.map((currency) => (
          <option key={currency} value={currency}>{currency}</option>
        ))}
      </select>
      <table>
        <thead>
          <tr>
            <th>Base</th>
            <th>Target</th>
            <th>Exchange Rate</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(exchangeRates.rates || {}).map(([targetCurrency, rate]) => (
            <tr key={targetCurrency}>
              <td>{exchangeRates.base_currency}</td>
              <td>{targetCurrency}</td>
              <td>{rate}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ExchangeRates;

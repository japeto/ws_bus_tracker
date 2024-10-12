import React, { useState, useEffect } from 'react';

const BusForm = ({ busData, onSubmit }) => {
  const [bus, setBus] = useState({
    name: '',
    capacity: '',
    licensePlate: '',
  });

  useEffect(() => {
    if (busData) {
      setBus(busData);
    }
  }, [busData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setBus({
      ...bus,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(bus);
  };

  return (
    <form onSubmit={handleSubmit} className="bus-form">
      <div className="form-group">
        <label>Nombre del Bus</label>
        <input
          type="text"
          name="name"
          value={bus.name}
          onChange={handleChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Capacidad</label>
        <input
          type="number"
          name="capacity"
          value={bus.capacity}
          onChange={handleChange}
          required
        />
      </div>

      <div className="form-group">
        <label>Placa</label>
        <input
          type="text"
          name="licensePlate"
          value={bus.licensePlate}
          onChange={handleChange}
          required
        />
      </div>

      <button type="submit">Guardar</button>
    </form>
  );
};

export default BusForm;

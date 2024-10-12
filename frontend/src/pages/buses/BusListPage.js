import React, { useState, useEffect } from 'react';
import { fetchBuses, createBus, updateBus, deleteBus } from '../../api/busApi';
import BusCard from '../../components/buses/busCard';
import BusForm from '../../components/buses/busForm';

const BusListPage = () => {
  const [buses, setBuses] = useState([]);
  const [selectedBus, setSelectedBus] = useState(null); // Para el modo de edición
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    const getBuses = async () => {
      const data = await fetchBuses();
      setBuses(data);
    };

    getBuses();
  }, []);

  const handleCreateOrUpdate = async (bus) => {
    if (isEditing) {
      await updateBus(selectedBus.id, bus);
    } else {
      await createBus(bus);
    }

    const updatedBuses = await fetchBuses();
    setBuses(updatedBuses);
    setSelectedBus(null);
    setIsEditing(false);
  };

  const handleEdit = (bus) => {
    setSelectedBus(bus);
    setIsEditing(true);
  };

  const handleDelete = async (id) => {
    await deleteBus(id);
    const updatedBuses = await fetchBuses();
    setBuses(updatedBuses);
  };

  return (
    <div>
      <h1>Lista de Buses</h1>
      {/* <BusForm busData={selectedBus} onSubmit={handleCreateOrUpdate} /> */}

      {/* Lista de buses */}
      <div className="bus-list">
        {buses.map((bus) => (
          <BusCard
            key={bus.id}
            bus={bus}
            onEdit={handleEdit}
            onDelete={handleDelete}
          />
        ))}
      </div>
    </div>
  );
};

export default BusListPage;

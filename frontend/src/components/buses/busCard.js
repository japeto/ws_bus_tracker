import React from 'react';
import styles from './busCard.module.css';

const BusCard = ({ bus, onEdit, onDelete }) => {
  return (
    <div className={styles.busCard}>
      <h3>{bus.plate}</h3>
      <p>Status: {bus.status}</p>
      <p>Plate: {bus.plate}</p>

      <div className={styles.busCardActions}>
        <button onClick={() => onEdit(bus)}>Editar</button>
        <button onClick={() => onDelete(bus.id)}>Eliminar</button>
      </div>
    </div>
  );
};

export default BusCard;

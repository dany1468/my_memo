import React from 'react';
import PropTypes from 'prop-types';

const UndeleteTodo = ({ lastDeletedTodo, undeleteTodo }) => {
  return (
    <div>
      <button
        type="button"
        onClick={undeleteTodo}
        className="todo-undelete"
        disabled={(Object.keys(lastDeletedTodo).length < 1)}
      >
        Undelete Todo
      </button>
    </div>
  );
};

UndeleteTodo.propTypes = {
  undeleteTodo: PropTypes.func.isRequired,
};

export default UndeleteTodo;

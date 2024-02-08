import './CardBtn.css'
function CardBtn({text}) {
  let btnClass = 'btn '

  function checkStatus() {
    if (text === 'Просмотрено') return btnClass += 'viewed'
    if (text === 'Отклик отправлен') return btnClass += 'enter'
    if (text === 'В резерве') return btnClass += 'reserve'
    return btnClass += 'viewed'
  }

  return (
    <button className={checkStatus()}>{text}</button>
  );
}

export default CardBtn;

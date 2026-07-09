const MEMBERS_KEY = 'members_database';

const initialMembers = [
  { id: 202410, matricula: '202410', name: 'Vitor', area: 'Dança', subLeader: true },
  { id: 202411, matricula: '202411', name: 'M. Eduarda', area: 'Roteiro - Figurino', subLeader: false },
  { id: 202412, matricula: '202412', name: 'Ana Clara', area: 'Staff', subLeader: false },
  { id: 202413, matricula: '202413', name: 'João Pedro', area: 'Comunicação', subLeader: false }
];

let members = getMembersFromDatabase();

const memberCount = document.querySelector('#member-count');
const memberList = document.querySelector('#member-list');
const promoteForm = document.querySelector('#promote-form');
const promoteUser = document.querySelector('#promote-user');
const promoteArea = document.querySelector('#promote-area');
const memberSearch = document.querySelector('#member-search');
const memberOptions = document.querySelector('#member-options');

promoteForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const typedMatricula = promoteUser.value.trim();
  const selectedMember = members.find((member) => member.matricula === typedMatricula);

  if (!selectedMember) {
    alert('Usuário não encontrado.');
    return;
  }

  selectedMember.area = promoteArea.value;
  selectedMember.subLeader = true;
  promoteForm.reset();
  saveMembersOnDatabase();
  renderMembers();
});

memberSearch.addEventListener('input', renderMembers);

renderMembers();

function getMembersFromDatabase() {
  const savedMembers = localStorage.getItem(MEMBERS_KEY);
  return savedMembers ? JSON.parse(savedMembers) : initialMembers;
}

function saveMembersOnDatabase() {
  localStorage.setItem(MEMBERS_KEY, JSON.stringify(members));
}

function renderMembers() {
  const searchTerm = memberSearch.value.toLowerCase();
  const visibleMembers = members.filter((member) => member.name.toLowerCase().includes(searchTerm));

  memberCount.textContent = members.length;
  memberOptions.innerHTML = members.map((member) => `<option value="${member.matricula}">${member.name}</option>`).join('');
  memberList.innerHTML = visibleMembers.map(createMemberRow).join('');

  document.querySelectorAll('.remove-button').forEach((button) => {
    button.addEventListener('click', () => {
      members = members.filter((member) => member.id !== Number(button.dataset.id));
      saveMembersOnDatabase();
      renderMembers();
    });
  });
}

function createMemberRow(member) {
  const subLeaderTag = member.subLeader ? '<span class="tag">Sub-Líder</span>' : '';

  return `
    <article class="member-row">
      <div class="member-avatar">${member.name.charAt(0)}</div>
      <div>
        <strong>${member.name}</strong>${subLeaderTag}
        <small>${member.matricula} - ${member.area}</small>
      </div>
      <button class="remove-button" data-id="${member.id}">Remover</button>
    </article>
  `;
}




const students = [
  { name: "Bhanu",  roll: 101, marks: { math: 85, english: 78, science: 92, history: 80 } },
  { name: "Prasad", roll: 102, marks: { math: 90, english: 88, science: 79, history: 95 } },
  { name: "Ravi",   roll: 103, marks: { math: 95, english: 82, science: 85, history: 89 } }
];

// 👉 Dynamically extract subjects from the marks object
const subjects = Object.keys(students[0].marks);

const toppers = {};

subjects.forEach(subject => {
  const winner = students.reduce(
    (max, student) => (student.marks[subject] > max.marks[subject] ? student : max),
    students[0]   // initial value
  );

  // Save only useful info
  toppers[subject] = {
    name: winner.name,
    roll: winner.roll,
    marks: winner.marks[subject]
  };
});

console.log(toppers);

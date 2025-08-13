const data = [
  { studentId: 1, name: "Rahul",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:85}, {subject:"Physics", marks:78}, {subject:"Chemistry", marks:82}]},
      { sem: 2, subjects: [{subject:"Math II", marks:81}, {subject:"Physics II", marks:76}, {subject:"Chemistry II", marks:80}]}
    ]
  },
  { studentId: 2, name: "Priya",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:90}, {subject:"Physics", marks:88}, {subject:"Chemistry", marks:91}]},
      { sem: 2, subjects: [{subject:"Math II", marks:95}, {subject:"Physics II", marks:92}, {subject:"Chemistry II", marks:89}]}
    ]
  },
  { studentId: 3, name: "Aisha",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:92}, {subject:"Physics", marks:81}, {subject:"Chemistry", marks:79}]},
      { sem: 2, subjects: [{subject:"Math II", marks:88}, {subject:"Physics II", marks:86}, {subject:"Chemistry II", marks:90}]}
    ]
  },
  { studentId: 4, name: "Vikram",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:76}, {subject:"Physics", marks:85}, {subject:"Chemistry", marks:84}]},
      { sem: 2, subjects: [{subject:"Math II", marks:79}, {subject:"Physics II", marks:87}, {subject:"Chemistry II", marks:85}]}
    ]
  },
  { studentId: 5, name: "Sneha",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:88}, {subject:"Physics", marks:90}, {subject:"Chemistry", marks:86}]},
      { sem: 2, subjects: [{subject:"Math II", marks:91}, {subject:"Physics II", marks:89}, {subject:"Chemistry II", marks:93}]}
    ]
  },
  { studentId: 6, name: "Rohit",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:94}, {subject:"Physics", marks:82}, {subject:"Chemistry", marks:88}]},
      { sem: 2, subjects: [{subject:"Math II", marks:90}, {subject:"Physics II", marks:84}, {subject:"Chemistry II", marks:86}]}
    ]
  },
  { studentId: 7, name: "Meera",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:80}, {subject:"Physics", marks:75}, {subject:"Chemistry", marks:77}]},
      { sem: 2, subjects: [{subject:"Math II", marks:83}, {subject:"Physics II", marks:78}, {subject:"Chemistry II", marks:79}]}
    ]
  },
  { studentId: 8, name: "Karan",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:87}, {subject:"Physics", marks:92}, {subject:"Chemistry", marks:90}]},
      { sem: 2, subjects: [{subject:"Math II", marks:86}, {subject:"Physics II", marks:94}, {subject:"Chemistry II", marks:88}]}
    ]
  },
  { studentId: 9, name: "Nisha",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:78}, {subject:"Physics", marks:80}, {subject:"Chemistry", marks:75}]},
      { sem: 2, subjects: [{subject:"Math II", marks:82}, {subject:"Physics II", marks:81}, {subject:"Chemistry II", marks:76}]}
    ]
  },
  { studentId: 10, name: "Arjun",
    semesters: [
      { sem: 1, subjects: [{subject:"Math", marks:91}, {subject:"Physics", marks:89}, {subject:"Chemistry", marks:87}]},
      { sem: 2, subjects: [{subject:"Math II", marks:93}, {subject:"Physics II", marks:90}, {subject:"Chemistry II", marks:92}]}
    ]
  }
];



function getTopStudentsBySubject(data) {
  const results = {};                     // 1. Create an empty object to hold the winners.

  data.forEach(student => {               // 2. Loop over each student in the input array.
    student.semesters.forEach(sem => {    // 3. For each student, loop over their semesters.
      if (!results[sem.sem]) results[sem.sem] = {}; // 4. Ensure `results` has an object for that semester (keyed by sem.sem).

      sem.subjects.forEach(sub => {       // 5. Loop over each subject in that semester.
        if (
          !results[sem.sem][sub.subject] ||    // 6a. If there's no current winner for this subject in that sem...
          sub.marks > results[sem.sem][sub.subject].marks // 6b. ...or this student's marks are greater than the recorded marks...
        ) {
          results[sem.sem][sub.subject] = {   // 7. ...update the winner for that subject+semester.
            student: student.name,
            marks: sub.marks
          };
        }
      });
    });
  });

  return results; // 8. Return the object that maps each semester -> subject -> { student, marks }.
}


console.log(getTopStudentsBySubject(data))





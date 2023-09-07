import {useState} from 'react' ;
import {StyleSheet, Text, View, Button, TextInput  } from 'react-native';

export default function App() {
  const [enteredGoalText, setEnteredGoalText] = useState("");
  const[courseGoals, setCourseGoals] = useState([]);

  function goalInputHandler(enteredText) {
    setEnteredGoalText(enteredText)
  };

  function addGoalHandler(enteredText) {
    setCourseGoals((currentCourseGoals) => [
      ...currentCourseGoals,
      enteredGoalText
    ]);
  };  

  return (
    <View style={styles.appContainer}>

      <View style={styles.inputContainer}>
        <TextInput style={styles.textInput} placeholder='Your Course Goal' onChangeText={goalInputHandler}/>
        <Button color={'green'} title='Add Goal' onPress={addGoalHandler}/>
      </View>

      <View style={styles.goalContainer}>
        {courseGoals.map((goal) => <Text key={goal}>{goal}</Text>)}
        <Text>List of Goals</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    paddingTop: 50,
    paddingHorizontal: 16
  },
 
  inputContainer: {
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 24,
    borderBottomWidth: 1,
    borderColor: '#ccccc'
  },

  textInput: {
    borderWidth: 1,
    borderColor: '#ccccc',
    marginRight: 10,
    padding: 5,
    width: '70%'
  },
  goalContainer: {
    flex: 8,
  }
});
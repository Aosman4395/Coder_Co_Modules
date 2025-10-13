user_input() {
    read -p "What team do you support? " team
    local team="$team"
    echo "You support $team"
}

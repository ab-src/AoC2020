def _convert_int(arg_str):
    arg = 0
    if arg_str[0] == "+":
        arg = int(arg_str[1:])
    elif arg_str[0] == "-":
        arg = int(arg_str)
        
    return arg

def parse_instruction(instruction):
    ins = instruction.split(" ")
    op = ins[0]
    arg = _convert_int(ins[1])

    return op, arg
    
def swap_instruction(instruction):
    ins = instruction.split(" ")  
    op = ins[0]
    if op == "nop":
        op = "jmp"
    elif op == "jmp":
        op = "nop"       
    arg = _convert_int(ins[1])

    return op, arg
    
def execute_instruction(op, arg, ins_ptr, accumulator=0):
    if op == "acc":
        accumulator += arg
        ins_ptr += 1
    elif op == "nop":
        ins_ptr += 1
    elif op == "jmp":
        ins_ptr += arg
        
    return accumulator, ins_ptr

def test_op_change(base_op, base_arg, ins_ptr, base_ptr, accumulator, executed_ins, program):
    changed_op, arg = swap_instruction(program[base_ptr])
    _, ins_ptr = execute_instruction(changed_op, arg, base_ptr)
    while ins_ptr < len(program):
        if ins_ptr in executed_ins:
            executed_ins = executed_ins[:base_ptr+1]
            accumulator, base_ptr = execute_instruction(base_op, base_arg, base_ptr, accumulator)
            break
        executed_ins.append(ins_ptr)
        op, arg = parse_instruction(program[ins_ptr])
        _, ins_ptr = execute_instruction(op, arg, ins_ptr)
    return changed_op, ins_ptr, base_ptr, accumulator, executed_ins
    
def day8_1(filename):
    accumulator = ins_ptr = 0
    executed_ins = []
    with open(filename, "r", encoding="utf-8") as input_file:
        program = list(input_file)
        while ins_ptr < len(program):
            if ins_ptr in executed_ins:
                break
            executed_ins.append(ins_ptr)
            op, arg = parse_instruction(program[ins_ptr])
            accumulator, ins_ptr = execute_instruction(op, arg, ins_ptr, accumulator)
            
    return accumulator
            
def day8_2(filename):
    accumulator = ins_ptr = base_ptr = found_ins_flag = 0
    executed_ins = []

    with open(filename, "r", encoding="utf-8") as input_file:
        program = list(input_file)
        
        while base_ptr < len(program):
            ins_ptr = base_ptr
            base_op, base_arg = parse_instruction(program[base_ptr])
            executed_ins.append(base_ptr)
            if base_op == "acc" or found_ins_flag == 1:
                accumulator, base_ptr = execute_instruction(base_op, base_arg, base_ptr, accumulator)
            else:
                changed_op, ins_ptr, base_ptr, accumulator, executed_ins = test_op_change(base_op, base_arg, ins_ptr, base_ptr, accumulator, executed_ins, program)
                if ins_ptr >= len(program):
                    found_ins_flag = 1
                    accumulator, base_ptr = execute_instruction(changed_op, base_arg, base_ptr, accumulator)
                
    return accumulator
  
print(day8_1("input.txt"))
print(day8_2("input.txt"))

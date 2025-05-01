# ComfyUI Nodes for Reprompted Shortcodes

from .chance_node import RepromptedChanceNode
from .choose_node import RepromptedChooseNode
from .else_node import RepromptedElseNode
from .eval_node import RepromptedEvalNode
from .file_node import RepromptedFileNode
from .get_node import RepromptedGetNode
from .if_node import RepromptedIfNode
from .override_node import RepromptedOverrideNode
from .random_node import RepromptedRandomNode
from .set_node import RepromptedSetNode

NODE_CLASS_MAPPINGS = {
    "RepromptedChanceNode": RepromptedChanceNode,
    "RepromptedChooseNode": RepromptedChooseNode,
    "RepromptedElseNode": RepromptedElseNode,
    "RepromptedEvalNode": RepromptedEvalNode,
    "RepromptedFileNode": RepromptedFileNode,
    "RepromptedGetNode": RepromptedGetNode,
    "RepromptedIfNode": RepromptedIfNode,
    "RepromptedOverrideNode": RepromptedOverrideNode,
    "RepromptedRandomNode": RepromptedRandomNode,
    "RepromptedSetNode": RepromptedSetNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RepromptedChanceNode": "Reprompted: Chance",
    "RepromptedChooseNode": "Reprompted: Choose",
    "RepromptedElseNode": "Reprompted: Else",
    "RepromptedEvalNode": "Reprompted: Eval",
    "RepromptedFileNode": "Reprompted: File",
    "RepromptedGetNode": "Reprompted: Get",
    "RepromptedIfNode": "Reprompted: If",
    "RepromptedOverrideNode": "Reprompted: Override",
    "RepromptedRandomNode": "Reprompted: Random",
    "RepromptedSetNode": "Reprompted: Set"
}
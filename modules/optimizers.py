import torch

# for IU Dataset
def build_optimizer(args, model):
    vef_params = list(map(id, model.resnet_f.parameters()))
    vel_params = list(map(id, model.resnet_l.parameters()))
    ed_params = filter(lambda x: id(x) not in vef_params + vel_params, model.parameters())
    optimizer = getattr(torch.optim, args.optim)(
        [{'params': model.resnet_f.parameters(), 'lr': args.lr_ve},
         {'params': model.resnet_l.parameters(), 'lr': args.lr_ve},
         {'params': ed_params, 'lr': args.lr_ed}],
        weight_decay=args.weight_decay,
        amsgrad=args.amsgrad
    )
    return optimizer


# for MIMIC Dataset
# def build_optimizer(args, model):
#     ve_params = list(map(id, model.resnet.parameters()))
#     ed_params = filter(lambda x: id(x) not in ve_params, model.parameters())
#     optimizer = getattr(torch.optim, args.optim)(
#         [{'params': model.resnet.parameters(), 'lr': args.lr_ve},
#          {'params': ed_params, 'lr': args.lr_ed}],
#         weight_decay=args.weight_decay,
#         amsgrad=args.amsgrad
#     )
#     return optimizer


def build_lr_scheduler(args, optimizer):
    lr_scheduler = getattr(torch.optim.lr_scheduler, args.lr_scheduler)(optimizer, args.step_size, args.gamma)
    return lr_scheduler
